#TODO:
#Split into subpackages, add descriptions

Summary:	GNOME games extra data
Summary(pl):	Dodatkowe grafiki dla gier GNOME
Name:		gnome-games-extra-data
Version:	2.7.0
Release:	0.1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	797b4fcff11e8674a6e75dc193fa597a
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
GNOME games extra data.

%description -l pl
Dodatkowe grafiki dla gier GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_pixmapsdir}/gnome-games-common/*
%{_pixmapsdir}/glines/*
%{_pixmapsdir}/gnobots2/*
%{_pixmapsdir}/gnometris/*
%{_pixmapsdir}/iagno/*
%{_pixmapsdir}/mahjongg/*
%{_pixmapsdir}/same-gnome/*
