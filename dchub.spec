Summary:	Direct Connect Hub
Summary(pl.UTF-8):	Serwer Direct Connect
Name:		dchub
Version:	0.5.2
Release:	14
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.homelinux.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	673a43cde95bce2c2acba2cfab83d527
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-init.patch
Patch2:		%{name}-crcdir.patch
Patch3:		%{name}-pic.patch
Patch4:		am.patch
Patch5:		format-security.patch
URL:		http://ac2i.homelinux.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
# for AM_PATH_GLIB macro
BuildRequires:	glib-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgcrypt-devel >= 1.1.12
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	perl-Locale-gettext
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dchub is a hub of direct connect file sharing network.

%description -l pl.UTF-8
dchub jest hubem sieci direct connect służącej do wymiany plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},/etc/rc.d/init.d,/var/lib/%{name}}
install dchub.init $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install plugin/AUTOSTART $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/AUTOSTART

# delete unnecesary files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/Makefile
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.c
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.h
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/po

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add dchub
%service dchub restart

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del dchub
	%service dchub stop
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc Documentation/{Global,commands,configuration_file,ext_prog,hub_cluster.postv0.4.0,plugin,protocol_extension,scripts,user_file}
%lang(de) %doc Documentation/*.de
%lang(fr) %doc Documentation/*.fr
%lang(nl) %doc Documentation/*.nl
%dir %{_sysconfdir}/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/tools
%attr(755,root,root) %{_libdir}/%{name}/tools/*
%dir %{_libdir}/%{name}/extprog
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/%{name}/extprog/AUTOSTART
%attr(755,root,root) %{_libdir}/%{name}/extprog/[CDPdm]*
%dir %{_libdir}/%{name}/plugins
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/%{name}/plugins/AUTOSTART
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%dir %{_libdir}/%{name}/scripts
%attr(755,root,root) %{_libdir}/%{name}/scripts/*.pl
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/%{name}/scripts/dchub_scripts.conf
%dir %{_libdir}/%{name}/scripts/i18n
%lang(de) %{_libdir}/%{name}/scripts/i18n/de
%lang(fr) %{_libdir}/%{name}/scripts/i18n/fr
%lang(hu) %{_libdir}/%{name}/scripts/i18n/hu
%lang(sv) %{_libdir}/%{name}/scripts/i18n/sv
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir /var/lib/%{name}
