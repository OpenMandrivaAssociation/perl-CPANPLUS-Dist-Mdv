%define upstream_name    CPANPLUS-Dist-Mdv
%define upstream_version 2.100400

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A cpanplus backend to build mandriva rpms
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(YAML)
BuildRequires:  perl(version)

Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
CPANPLUS::Dist::Mdv is a distribution class to create mandriva packages from
CPAN modules, and all its dependencies. This allows you to have the most recent
copies of CPAN modules installed, using your package manager of choice, but
without having to wait for central repositories to be updated.

You can either install them using the API provided in this package, or manually
via rpm.

Some of the bleading edge CPAN modules have already been turned into mandriva
packages for you, and you can make use of them by adding the cooker
repositories (main & contrib).

Note that these packages are built automatically from CPAN and are assumed to
have the same license as perl and come without support. Please always refer to
the original CPAN package if you have questions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CPANPLUS
%{perl_vendorlib}/auto
%{_mandir}/*/*
