terraform {
  #backend "local" {}
  backend "remote" {
    # The name of your Terraform Cloud organization.
    organization = "nabla"

    # The name of the Terraform Cloud workspace to store Terraform state files in.
    workspaces {
      name = "petclinic-native"
    }
  }
}
