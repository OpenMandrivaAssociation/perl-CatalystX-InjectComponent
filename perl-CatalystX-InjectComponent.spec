%define upstream_name    CatalystX-InjectComponent
%define upstream_version 0.025

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.025
Release:	1

Summary:	Inject components into your Catalyst application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CatalystX/CatalystX-InjectComponent-0.025.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Devel::InnerPackage)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(parent)
BuildArch:	noarch

%description
CatalystX::InjectComponent will inject Controller, Model, and View
components into your Catalyst application at setup (run)time. It does this
by creating a new package on-the-fly, having that package extend the given
component, and then having Catalyst setup the new component (via
'->setup_component')

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


