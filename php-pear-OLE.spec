# ToDo:
# - pl description
%include	/usr/lib/rpm/macros.php
%define         _class          OLE
%define		_status		alpha
%define		_pearname	%{_class}
Summary:	%{_pearname} - Package for reading and writing OLE containers
Summary(pl):	%{_pearname} - Pakiet do odczytu i zapisu kontenerów OLE
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
# Source0-md5:	0684be1d8b21c64bfab65894ca392fc9
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows reading and writing of OLE (Object Linking and
Embedding) files, the format used as container for Excel, Word and
other MS file formats. Documentation for the OLE format can be found
at: http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html

This class has in PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,PPS}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/PPS/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/PPS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/PPS
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/PPS/*.php
