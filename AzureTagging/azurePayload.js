// Script step in ServiceNow which must be accompanied by a REST step, with the outputObject, inside of an action.
// Add more variables as needed.
(function execute(inputs, outputs) {
    var outputObject = {
        vm_name: inputs.serverGR.name.getDisplayValue(),
        business_unit: inputs.serverGR.company.getDisplayValue(),
        cost_center: inputs.serverGR.cost_center.getDisplayValue(),
        owned_by: inputs.serverGR.owned_by.email.getDisplayValue(),
        install_status: inputs.serverGR.install_status.getDisplayValue(),
        classification: inputs.serverGR.classification.getDisplayValue(),
        os: inputs.serverGR.os.getDisplayValue(),
        purpose: inputs.serverGR.short_description.getDisplayValue(),
        location: inputs.serverGR.location.getDisplayValue()
    };

    outputs.outputjson = JSON.stringify(outputObject);

})(inputs, outputs);
