# Created by pyp2rpm-1.1.2 and rewrote manually afterwards
%global pypi_name docker-pycreds

# the test suite is diabled b/c it needs docker-credential-secretservice binary
# and we don't have that now (Sep 2016) in Fedora
%bcond_with tests

Name:           python-%{pypi_name}
Version:	0.4.0
Release:        4%{?dist}
Summary:        Python bindings for the docker credentials store API

License:        ASL 2.0
URL:            https://github.com/shin-/dockerpy-creds/
Source0:	https://files.pythonhosted.org/packages/c5/e6/d1f6c00b7221e2d7c4b470132c931325c8b22c51ca62417e300f5ce16009/docker-pycreds-0.4.0.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six
Requires: 	python-six


%description
Python bindings for the docker credentials store API


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build

%install
%py3_install

%{__python} -c "import dockerpycreds"

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/dockerpycreds
%{python3_sitelib}/docker_pycreds-%{version}-py?.?.egg-info
