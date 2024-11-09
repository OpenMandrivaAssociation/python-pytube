%define module pytube
Summary:	pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
Name:		python-pytube
Version:	15.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytube/pytube-%{version}.tar.gz
License:	The Unlicense
Group:		Development/Python
Url:		https://pytube.io/
Provides:	%{module}
BuildRequires:	pkgconfig(python)
BuildArch:	noarch

%description
A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos. 

#--------------------------------------------------------------------

%files
%{python_sitelib}/pytube-%{version}-py*.*.egg-info
%{python_sitelib}/pytube//
#--------------------------------------------------------------------

%prep
%autosetup -n pytube-%{version} -p1

%build
%py_build

%install
%py_install
