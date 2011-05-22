%define name gnome-xcf-thumbnailer
%define version 1.0
%define release %mkrel 4

Summary: Thumbnailer for GIMP's own format, XCF files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/%name/%{name}-%{version}.tar.bz2
Patch0: gnome-xcf-thumbnailer-1.0-link.patch
License: GPLv2
Group: File tools
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libpng-devel
BuildRequires: glib2-devel >= 2.16
BuildRequires: libGConf2-devel
BuildRequires: popt-devel

%description
This creates thumbnail images from Gimp's XCF image files for nautilus and
other file managers.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post
%post_install_gconf_schemas %name
%preun
%preun_uninstall_gconf_schemas %name

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name

