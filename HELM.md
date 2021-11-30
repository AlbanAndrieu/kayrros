# helm

# Table of contents

<!-- toc -->

- [petclinic](#petclinic)
  * [k8s version issue](#k8s-version-issue)
  * [Create helm package](#create-helm-package)
  * [Install helm package](#install-helm-package)

<!-- tocstop -->

# petclinic

## k8s version issue

```shell
kubectlxx version --short
Client Version: v1.22.3-3+9ec7c40ec93c73
Server Version: v1.22.3-3+9ec7c40ec93c73
```

I recently upgrade k8s on my workstation, ingress API changes

See https://kubernetes.io/fr/docs/concepts/services-networking/ingress/

## Create helm package

```shell
helm lint packs/helm-petclinic/charts/
helm package ./packs/helm-petclinic/charts
```

## Install helm package

```shell
helm uninstall --kubeconfig ${HOME}/.kube/config --kube-context microk8s --namespace jenkins my-petclinic helm-petclinic-1.0.0.tgz
helm install --kubeconfig ${HOME}/.kube/config --kube-context microk8s --namespace jenkins my-petclinic helm-petclinic-1.0.0.tgz --timeout 5m0s --wait --atomic
helm install --kubeconfig ${HOME}/.kube/config --kube-context microk8s --namespace jenkins my-petclinic helm-petclinic-1.0.0.tgz --timeout 5m0s --wait --atomic --devel --replace --dependency-update --set imagePullPolicy=Always
```

See result on https://github.com/AlbanAndrieu/spring-petclinic/releases/tag/helm-petclinic-1.0.0
