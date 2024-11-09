%define module pytube
Summary:	pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
Name:		python-pytube
Version:	15.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytube/pytube-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pytube.io/
Provides:	%{module}
BuildRequires:	pkgconfig(python)
BuildArch:	noarch

%description
A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos. 

#--------------------------------------------------------------------

%files
#{python_sitelib}/pypdf-%{version}.dist-info
#{python_sitelib}/pypdf/
#--------------------------------------------------------------------

%prep
%autosetup -n pypdf-%{version} -p1

%build
%py_build

%install
%py_install
