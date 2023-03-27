Challenge #2
We need to write code that will query the meta data of an instance within GCP and provide a
json formatted output.

provider "google" {
project = "spring-iris-381706"
}

resource "google_compute_instance" "appserver" {
  name         = "appserver"
  machine_type = "e2-medium"
  zone         = "us-east4-c"

  tags = ["foo", "bar"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "value"
      }
    }
  }

  network_interface {
    network = "three-tier-vpc"
	subnetwork = "three-tier-middle-subnet"

    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    class = "optimized"
  }

}
output "instance_metadata" {
  value = jsonencode(resource.google_compute_instance.appserver.metadata)
}


