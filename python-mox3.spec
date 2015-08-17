# Created by pyp2rpm-1.1.1
%global pypi_name mox3

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        2%{?dist}
Summary:        Mock object framework for Python

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# https://bugs.launchpad.net/heat-cfntools/+bug/1403214/
BuildArch:      noarch
 
Requires:  python-pbr >= 1.3.0

BuildRequires:  python2-devel
BuildRequires:  python-pbr >= 1.3.0
BuildRequires:  python-nose
BuildRequires:  python-testrepository
 
%if 0%{?with_python3}
Requires:  python3-pbr >= 1.3.0

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.3.0
BuildRequires:  python3-nose
BuildRequires:  python3-testrepository
%endif


%description
Mox3 is a mock object framework for Python 3 and 2.7.
Mox3 is an unofficial port of the Google mox framework to Python 3. It was
meant to be as compatible with mox as possible, but small enhancements have
been made.

This is Python 2 version.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Mock object framework for Python


%description -n python3-%{pypi_name}
Mox3 is a mock object framework for Python 3 and 2.7.
Mox3 is an unofficial port of the Google mox framework to Python 3. It was
meant to be as compatible with mox as possible, but small enhancements have
been made.

This is Python 3 version.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}

pushd %{py3dir}
popd
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests-%{python2_version}

%if 0%{?with_python3}
pushd %{py3dir}
nosetests-%{python3_version}
popd
%endif

%files
%doc README.rst
%license COPYING.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif


%changelog
* Mon Aug 17 2015 Alan Pevec <apevec.pevec@redhat.com> 0.9.0-2
- package review feedback

* Sun Aug 16 2015 Alan Pevec <alan.pevec@redhat.com> 0.9.0-1
- Update to upstream 0.9.0

* Tue Dec 16 2014 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-1
- Initial package.
