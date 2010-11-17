%define sampledir $RPM_BUILD_ROOT/opt/sample-media/Images

Name: meego-cursor-theme
Version: 0.4
Release: %mkrel 1
Summary: MeeGo X cursors icon theme
Group: Graphics
License: CC-BY
URL: http://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xcursorgen
BuildArch: noarch
Obsoletes: moblin-cursor-theme <= 0.3

%description
MeeGo X cursors icon theme.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/moblin/cursors
cp -r xcursors/* %{buildroot}%{_datadir}/icons/moblin/cursors

%clean
rm -rf %{buildroot}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%postun
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_datadir}/icons/moblin/
