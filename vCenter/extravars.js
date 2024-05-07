// Extra variables from ServiceNow pushed to Ansible.
// Add more variables as needed. 
var vm_name_sys = fd_data.trigger.current.name;
var business_unit_sys = fd_data.trigger.current.company;
var cost_center_sys = fd_data.trigger.current.cost_center;
var owned_by_sys = fd_data.trigger.current.owned_by;
var install_status_sys = fd_data.trigger.current.install_status;
var environment_sys = fd_data.trigger.current.classification;
var location_sys = fd_data.trigger.current.location;
var os_sys = fd_data.trigger.current.os;

var payload = {
    vm_name: vm_name_sys.getDisplayValue().toUpperCase(),
    business_unit: business_unit_sys.getDisplayValue(),
    cost_center: cost_center_sys.getDisplayValue(),
    owned_by: owned_by_sys.getDisplayValue(),
    install_status: install_status_sys.getDisplayValue(),
    classification: environment_sys.getDisplayValue(),
    location: location_sys.getDisplayValue(),
    os: os_sys.getDisplayValue()
};

return JSON.stringify(payload);
