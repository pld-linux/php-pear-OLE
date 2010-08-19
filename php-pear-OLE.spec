%include	/usr/lib/rpm/macros.php
%define		_class		OLE
%define		_status		beta
%define		_pearname	%{_class}
%define		subver	RC1
%define		rel		1
Summary:	%{_pearname} - package for reading and writing OLE containers
Summary(pl.UTF-8):	%{_pearname} - pakiet do odczytu i zapisu kontenerów OLE
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	232a44e1da145afc6f6a5b791ae605f8
URL:		http://pear.php.net/package/OLE/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows reading and writing of OLE (Object Linking and
Embedding) files, the format used as container for Excel, Word and
other MS file formats. Documentation for the OLE format can be found
at: <http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet pozwala na odczyt i zapis plików OLE (Object Linking and
Embedding), formatu używanego jako kontener dla Excela, Worda i innych
formatów plików MS. Dokumentację dla formatu OLE można znaleźć pod
<http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}
