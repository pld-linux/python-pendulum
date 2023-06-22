# Conditional build:
%bcond_with	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pendulum

Summary:	Python datetimes made easy
Name:		python-%{module}
Version:	2.1.2
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pendulum/%{module}-%{version}.tar.gz
# Source0-md5:	b5c76f3b4253666e964ca9ec6251928d
URL:		https://pypi.python.org/project/pendulum
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:61.0.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python datetimes made easy.

%package -n python3-%{module}
Summary:	Python datetimes made easy
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Python datetimes made easy.

%prep
%setup -q -n %{module}-%{version}
cat > setup.py <<EOF
from setuptools import setup
setup(version='%{version}')
EOF

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
