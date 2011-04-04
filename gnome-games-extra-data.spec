%define		games_ver	1:3.0.0
Summary:	GNOME games extra data
Summary(pl.UTF-8):	Dodatkowe grafiki dla gier GNOME
Name:		gnome-games-extra-data
Version:	3.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games-extra-data/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	0fdd978671120a7b01daf11a9f525adb
URL:		http://www.gnome.org/
Requires:	gnome-games >= %{games_ver}
Conflicts:	gnome-games < 2.7.7
Obsoletes:	gnome-games-extra-data-gnometris
Obsoletes:	gnome-games-extra-data-same-gnome
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

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
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

%files iagno
%defattr(644,root,root,755)
%{_datadir}/gnome-games/iagno/pixmaps/*.png

%files mahjongg
%defattr(644,root,root,755)
%{_datadir}/gnome-games/mahjongg/pixmaps/*.png
