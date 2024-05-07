import os
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsResource
from azure.mgmt.compute import ComputeManagementClient
import logging

# A dictionary to map the keys from request body to the required tag names
tag_key_map = {
    "business_unit": "BU",
    "cost_center": "Cost Center",
    "owned_by": "Owner",
    "install_status": "Install Status",
    "classification": "Classification",
    "location": "Location"
}

def apply_tags_to_vm(vm_name, tags):
    credential = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    resource_client = ResourceManagementClient(credential, subscription_id)
    try:
        vm_resource_group = get_resource_group(vm_name)
        if vm_resource_group is None:
            raise Exception(f"Resource group for VM {vm_name} not found")
        vm_resource_id = (f"/subscriptions/{subscription_id}/resourceGroups/"
                          f"{vm_resource_group}/providers/Microsoft.Compute/virtualMachines/{vm_name}")
        resource_client.tags.update_at_scope(vm_resource_id, TagsResource(tags=tags))
        return True, f"Tags {tags} were added to VM {vm_name} in resource group {vm_resource_group}"
    except Exception as e:
        return False, str(e)

# Find the name of the resource group the VM is in. 
def get_resource_group(vm_name):
    credential = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    compute_client = ComputeManagementClient(credential, subscription_id)
    try:
        vms = compute_client.virtual_machines.list_all()
        for vm in vms:
            if vm.name.lower() == vm_name.lower():
                return vm.id.split('/')[4]
        raise Exception(f"VM {vm_name} not found in any resource group")
    except Exception as e:
        logging.error(f"Error getting resource group for VM {vm_name}: {str(e)}")
        return None

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        # Translate the tags using tag_key_map
        tags_to_apply = {tag_key_map[k]: v for k, v in req_body.items() if k in tag_key_map and v is not None}

        # Check if the required 'vm_name' key exists
        vm_name = req_body.get('vm_name')
        if not vm_name:
            raise ValueError("Key 'vm_name' not found in request")

        success, message = apply_tags_to_vm(vm_name, tags_to_apply)
        if success:
            return func.HttpResponse(message, status_code=200)
        else:
            return func.HttpResponse(message, status_code=500)
    except ValueError as ve:
        # Captures the missing 'vm_name' key situation and returns a 400 Bad Request
        return func.HttpResponse(f"Error: {str(ve)}", status_code=400)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
