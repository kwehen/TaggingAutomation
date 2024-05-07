# Automating Resource Tagging with CMDB, Ansible, and Azure

This repository contains the code used in the blog post about automating resource tagging using a Configuration Management Database (CMDB), Ansible, and Azure.

## Overview

The blog post discusses the importance of having a CMDB and implementing a tagging system for IT assets and services. It provides a guide on how to automate tagging out of the CMDB into Azure and/or vCenter using ServiceNow, AWX or Ansible Tower, and Azure Functions.

## Prerequisites

- ServiceNow + Midservers
- AWX or Ansible Tower
- Service account with vSphere tagging permissions
- Azure subscription
- Azure Function with Tagging Contributor/Reader over your specified scope

## Flow Design

The automation is simple, on creation or update of a server record in the CMDB, the specified fields will be grabbed and posted to Ansible or Azure to tag the VMs.

## Code

The repository includes:

- An Ansible playbook for creating categories and assigning tags to the VM in vCenter
- JavaScript functions for taking variables/fields out of ServiceNow
- A Python Azure Function for applying tags to a VM in Azure

Please refer to the individual files for the code.

## Disclaimer

This guide shows how resource tagging can be done at no additional cost. However, depending on your organization's needs and resources, you might opt for paid solutions like the ITOM module from ServiceNow.
