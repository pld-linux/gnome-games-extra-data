# TODO:
#   - add descriptions
#
Summary:	GNOME games extra data
Summary(pl):	Dodatkowe grafiki dla gier GNOME
Name:		gnome-games-extra-data
Version:	2.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	797b4fcff11e8674a6e75dc193fa597a
URL:		http://www.gnome.org/
Requires:	gnome-games >= 2.7.7
Conflicts:	gnome-games < 2.7.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
GNOME games extra data.

%description -l pl
Dodatkowe grafiki dla gier GNOME.

%package glines
Summary:	Extra data for glines game
Summary(pl):	Dodatkowe grafiki dla gry glines
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-glines

%description glines
Extra data for glines game.

%description glines -l pl
Dodatkowe grafiki dla gry glines.

%package gnobots2
Summary:	Extra data for gnobots2 game
Summary(pl):	Dodatkowe grafiki dla gry gnobots2
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-gnobots2

%description gnobots2
Extra data for gnobots2 game.

%description gnobots2 -l pl
Dodatkowe grafiki dla gry gnobots2.

%package gnometris
Summary:	Extra data for gnometris game
Summary(pl):	Dodatkowe grafiki dla gry gnometris
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-gnometris

%description gnometris
Extra data for gnometris game.

%description gnometris -l pl
Dodatkowe grafiki dla gry gnometris.

%package iagno
Summary:	Extra data for iagno game
Summary(pl):	Dodatkowe grafiki dla gry iagno
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-iagno

%description iagno
Extra data for iagno game.

%description iagno -l pl
Dodatkowe grafiki dla gry iagno.

%package mahjongg
Summary:	Extra data for mahjongg game
Summary(pl):	Dodatkowe grafiki dla gry mahjongg
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-mahjongg

%description mahjongg
Extra data for mahjongg game.

%description mahjongg -l pl
Dodatkowe grafiki dla gry mahjongg.

%package same-gnome
Summary:	Extra data for same-gnome game
Summary(pl):	Dodatkowe grafiki dla gry same-gnome
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-same-gnome

%description same-gnome
Extra data for same-gnome game.

%description same-gnome -l pl
Dodatkowe grafiki dla gry same-gnome.

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

%files glines
%defattr(644,root,root,755)
%{_pixmapsdir}/glines/*

%files gnobots2
%defattr(644,root,root,755)
%{_pixmapsdir}/gnobots2/*

%files gnometris
%defattr(644,root,root,755)
%{_pixmapsdir}/gnometris/*

%files iagno
%defattr(644,root,root,755)
%{_pixmapsdir}/iagno/*

%files mahjongg
%defattr(644,root,root,755)
%{_pixmapsdir}/mahjongg/*

%files same-gnome
%defattr(644,root,root,755)
%{_pixmapsdir}/same-gnome/*
