Summary:	The IceWM Control Center
Summary(pl):	Centrum Sterowania IceWM'a
Name:		icecc
Version:	0.5
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://www.selena.kherson.ua/xvadim/programse.html#icecc
BuildRequires:	qt-devel
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The IceWM Control Center allows you to run various tools for
configuring IceWM's options.

%description -l pl
Centrum Sterowania IceWM pozwala na uruchomienie ró¿nych narzêdzi w
celu skonfigurowania opcji IceWM'a.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

install icecc/icecc $RPM_BUILD_ROOT%{_bindir}
install icecc/lo32-app-icecc.png $RPM_BUILD_ROOT%{_pixmapsdir}/icecc.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

gzip -9nf AUTHORS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz icecc/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Settings/IceWM/*
