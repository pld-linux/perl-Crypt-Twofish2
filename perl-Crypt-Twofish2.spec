#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Twofish2
Summary:	Crypt::Twofish2 - Crypt::CBC compliant Twofish encryption Perl module
Summary(pl):	Crypt::Twofish2 - perlowy modu³ szyfru Twofish zgodny z Crypt::CBC
Name:		perl-Crypt-Twofish2
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the Twofish cipher in a less braindamaged
(read: slow and ugly) way than the existing "Crypt::Twofish" module.
Although it is "Crypt::CBC" compliant you usually gain nothing by
using that module (except generality), since "Crypt::Twofish2" can
work in either ECB or CBC mode.

%description -l pl
Ten modu³ jest implementacj± szyfru Twofish w mniej debilny (powolny
i paskudny) sposób ni¿ modu³ Crypt::Twofish. Pomimo tego, ¿e jest
zgodny z Crypt::CBC, nie ma potrzeby u¿ywania tamtego modu³u, poniewa¿
Crypt::Twofish2 mo¿e dzia³aæ zarówno w trybie ECB jak i CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/Twofish2.pm
%dir %{perl_sitearch}/auto/Crypt/Twofish2
%{perl_sitearch}/auto/Crypt/Twofish2/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Twofish2/*.so
%{_mandir}/man3/*
