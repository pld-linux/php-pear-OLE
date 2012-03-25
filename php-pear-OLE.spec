%define		status		beta
%define		pearname	OLE
%define		subver	RC2
%define		rel		1
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - package for reading and writing OLE containers
Summary(pl.UTF-8):	%{pearname} - pakiet do odczytu i zapisu kontenerów OLE
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}%{subver}.tgz
# Source0-md5:	5ef0283689ddf6b41de0588bce995c89
URL:		http://pear.php.net/package/OLE/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows reading and writing of OLE (Object Linking and
Embedding) files, the format used as container for Excel, Word and
other MS file formats. Documentation for the OLE format can be found
at: <http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html>.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet pozwala na odczyt i zapis plików OLE (Object Linking and
Embedding), formatu używanego jako kontener dla Excela, Worda i innych
formatów plików MS. Dokumentację dla formatu OLE można znaleźć pod
<http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html>.

Ta klasa ma w PEAR status: %{status}.

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
%{php_pear_dir}/OLE.php
%{php_pear_dir}/OLE
