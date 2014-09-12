#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Twofish2
Summary:	Crypt::Twofish2 - Crypt::CBC compliant Twofish encryption Perl module
Summary(pl.UTF-8):	Crypt::Twofish2 - perlowy moduł szyfru Twofish zgodny z Crypt::CBC
Name:		perl-Crypt-Twofish2
Version:	1.02
Release:	3
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28efe17baac40c14914912bb3e5932b5
URL:		http://search.cpan.org/dist/Crypt-Twofish2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the Twofish cipher in a less braindamaged
(read: slow and ugly) way than the existing "Crypt::Twofish" module.
Although it is "Crypt::CBC" compliant you usually gain nothing by
using that module (except generality), since "Crypt::Twofish2" can
work in either ECB or CBC mode.

%description -l pl.UTF-8
Ten moduł jest implementacją szyfru Twofish w mniej debilny (powolny
i paskudny) sposób niż moduł Crypt::Twofish. Pomimo tego, że jest
zgodny z Crypt::CBC, nie ma potrzeby używania tamtego modułu, ponieważ
Crypt::Twofish2 może działać zarówno w trybie ECB jak i CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Twofish2.pm
%dir %{perl_vendorarch}/auto/Crypt/Twofish2
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Twofish2/*.so
%{_mandir}/man3/*
