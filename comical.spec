Name: comical
Version: 0.8
Release: 8%{?dist}
Summary: GUI comic book viewer
License: GPLv2
Group: Applications/Multimedia
URL: http://comical.sourceforge.net/
Source0: http://download.sourceforge.net/comical/comical-%{version}.tar.gz
Source1: comical.png
Source2: comical.desktop
Patch0: comical-0.8-jpe.patch
Patch1: comical-0.8-optflags.patch
Patch2: comical-0.8-wxicon.patch
Patch3: comical-0.8-libunrar.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: wxGTK2-devel
BuildRequires: desktop-file-utils
BuildRequires: libunrar-devel


%description
Comical is a fully featured GUI comic book viewer using wxWidgets. It 
can view CBZ and CBR format files.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
rm -rf unrar


%build
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 comical %{buildroot}%{_bindir}

install -p -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE2}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO
%{_bindir}/comical
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Sat Oct 25 2008 Andreas Thienemann <andreas@bawue.net> - 0.8-8
- Removed use of private libunrar copy, use systemwide one.

* Thu Oct 16 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8-7
- rebuild

* Sat Sep 27 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8-6
- Fix building with latest wxWidgets

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8-5
- rebuild

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.8-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Andreas Thienemann <andreas@bawue.net> 0.8-3
- Bump for rebuild.

* Mon Jul 31 2006 Andreas Thienemann <andreas@bawue.net> 0.8-2
- Import into livna due to libunrar licensing issues.
- Bumped to 0.8-2

* Mon Apr 24 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.8-1
- bump for 0.8

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.7-2
- bump for FC5

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.7-1
- bump to 0.7
- disable all the sort patches, the 0.7 sort is no better than the 
  original 0.4 sort, but they changed how they did it, so the old sort
  patches would have to be reworked... and I'm not motivated right now.

* Sat Jun  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-9
- fix x86_64 by not using std::min

* Fri Jun  3 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-8
- add dist tag

* Sun Apr 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-7
- Support images that end in ".jpe". Most likely, .jpeg files that 
  were truncated by saving/compressing.

* Sat Apr  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-6
- Minor spec cleanups.

* Sat Apr  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-5
- Enhance the sort algorithm to be more intelligent.

* Mon Apr  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-4
- drop --with-gtk from configure, unused
- backout "bracket" patch, it breaks if [ or ] are in the directory path

* Mon Apr  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-3
- Add sort menu option to enable/disable sorting of images in archive
- Add logo from Brian Pepple
- Add desktop entry
- Add patch to gracefully deal with the absence of unrar

* Sun Apr  3 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-2
- patch for handling files with [ or ] in their names

* Sun Apr  3 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-1
- inital package for Fedora Extras
- CBR support only works with unrar, but we can't have that as a dep
  due to licensing issues with unrar.
