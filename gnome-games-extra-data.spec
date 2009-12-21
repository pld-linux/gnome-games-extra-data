%define		games_ver	1:2.28.0
Summary:	GNOME games extra data
Summary(pl.UTF-8):	Dodatkowe grafiki dla gier GNOME
Name:		gnome-games-extra-data
Version:	2.28.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games-extra-data/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	a9f6ca8a2ae28659feb4ee3254020115
URL:		http://www.gnome.org/
Requires:	gnome-games >= %{games_ver}
Conflicts:	gnome-games < 2.7.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME games extra data.

%description -l pl.UTF-8
Dodatkowe grafiki dla gier GNOME.

%package glines
Summary:	Extra data for glines game
Summary(pl.UTF-8):	Dodatkowe grafiki dla gry glines
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-glines >= %{games_ver}

%description glines
Extra data for glines game.

%description glines -l pl.UTF-8
Dodatkowe grafiki dla gry glines.

%package gnobots2
Summary:	Extra data for gnobots2 game
Summary(pl.UTF-8):	Dodatkowe grafiki dla gry gnobots2
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-gnobots2 >= %{games_ver}

%description gnobots2
Extra data for gnobots2 game.

%description gnobots2 -l pl.UTF-8
Dodatkowe grafiki dla gry gnobots2.

%package gnometris
Summary:	Extra data for gnometris game
Summary(pl.UTF-8):	Dodatkowe grafiki dla gry gnometris
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-gnometris >= %{games_ver}

%description gnometris
Extra data for gnometris game.

%description gnometris -l pl.UTF-8
Dodatkowe grafiki dla gry gnometris.

%package iagno
Summary:	Extra data for iagno game
Summary(pl.UTF-8):	Dodatkowe grafiki dla gry iagno
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-iagno >= %{games_ver}

%description iagno
Extra data for iagno game.

%description iagno -l pl.UTF-8
Dodatkowe grafiki dla gry iagno.

%package mahjongg
Summary:	Extra data for mahjongg game
Summary(pl.UTF-8):	Dodatkowe grafiki dla gry mahjongg
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-mahjongg >= %{games_ver}

%description mahjongg
Extra data for mahjongg game.

%description mahjongg -l pl.UTF-8
Dodatkowe grafiki dla gry mahjongg.

%package same-gnome
Summary:	Extra data for same-gnome game
Summary(pl.UTF-8):	Dodatkowe grafiki dla gry same-gnome
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-games-same-gnome >= %{games_ver}

%description same-gnome
Extra data for same-gnome game.

%description same-gnome -l pl.UTF-8
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
%{_datadir}/gnome-games-common/cards

%files glines
%defattr(644,root,root,755)
%{_datadir}/gnome-games/glines/pixmaps/*.png

%files gnobots2
%defattr(644,root,root,755)
%{_datadir}/gnome-games/gnobots2/themes/*.png

%files gnometris
%defattr(644,root,root,755)
%{_datadir}/gnome-games/gnometris/pixmaps/*.png

%files iagno
%defattr(644,root,root,755)
%{_datadir}/gnome-games/iagno/pixmaps/*.png

%files mahjongg
%defattr(644,root,root,755)
%{_datadir}/gnome-games/mahjongg/pixmaps/*.png

%files same-gnome
%defattr(644,root,root,755)
%{_datadir}/gnome-games/same-gnome/themes/*/*.png
%{_datadir}/gnome-games/same-gnome/themes/*/*.svg
