Summary:	User switching plugin for Xfce desktop environment
Name:		xfswitch-plugin
Version:	0.0.1
Release:	11
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfswitch-plugin/
Source0:	http://goodies.xfce.org/releases/xfswitch-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4-panel-devel >= 4.7.0
BuildRequires:	pkgconfig(libxfcegui4-1.0)
Requires:	gdm

%description
Xfswitch-plugin is a user switching plugin, which allows you 
to leave the current session opened and open a new session 
with another user.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/%{name}.desktop


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 0.0.1-10mdv2012.0
+ Revision: 791574
- Rebuild

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-9
+ Revision: 789931
- rebuild
- drop old stuff from spec file

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-8
+ Revision: 633064
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-7mdv2011.0
+ Revision: 579683
- rebuild for new xfce 4.7.0

* Sun Aug 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-6mdv2011.0
+ Revision: 564729
- rebuild

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-5mdv2010.1
+ Revision: 543317
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.0.1-4mdv2010.0
+ Revision: 446160
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-3mdv2009.1
+ Revision: 349262
- rebuild whole xfce

* Mon Feb 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-2mdv2009.1
+ Revision: 338873
- looks like package got lost in space

* Sun Feb 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-1mdv2009.1
+ Revision: 338612
- add source and spec files
- Created package structure for xfswitch-plugin.

