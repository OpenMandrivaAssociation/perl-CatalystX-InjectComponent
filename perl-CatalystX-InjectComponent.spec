%define upstream_name    CatalystX-InjectComponent
%define upstream_version 0.024

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Inject components into your Catalyst application
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CatalystX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Devel::InnerPackage)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Most)
BuildRequires: perl(parent)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
CatalystX::InjectComponent will inject Controller, Model, and View
components into your Catalyst application at setup (run)time. It does this
by creating a new package on-the-fly, having that package extend the given
component, and then having Catalyst setup the new component (via
'->setup_component')

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

