Summary:	The IceWM Control Center
Summary(pl):	Centrum Sterowania IceWM-a
Name:		icecc
Version:	1.5
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
# Source0-md5:	d825160422af53575488257814e36d19
Source1:	%{name}.desktop
URL:		http://www.selena.kherson.ua/xvadim/programse.html#icecc
BuildRequires:	qt-devel >= 3.0.5
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The IceWM Control Center allows you to run various tools for
configuring IceWM's options.

%description -l pl
Centrum Sterowania IceWM pozwala na uruchomienie ró¿nych narzêdzi w
celu skonfigurowania opcji IceWM-a.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README icecc/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Settings/IceWM/*
