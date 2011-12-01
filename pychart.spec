%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		pychart
Version:	1.39
Release:	10.1%{?dist}
License:	GPLv2+
Group:		System Environment/Libraries
Summary:	Python library for generating chart images
URL:		http://home.gna.org/pychart/
# This is the good upstream source. Unfortunately, we need to remove the dot to make latex2html happy.
# Source0:	http://download.gna.org/pychart/PyChart-%{version}.tar.gz
Source0:	PyChart-1_39.tar.gz
# Fedora Core Python doesn't include the Doc/* directory in any binary package, so we can't build without
# it as an addon source tarball. This is BZ #177350
Source1:	python-2.4.2-Doc.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	ghostscript-devel, tetex-latex, latex2html, python-devel, python-tools
BuildArch:	noarch
Patch0:		pychart-1.39-mkhowto.patch
Patch1:         pychart-1.39-optparse.patch
%description
PyChart is a Python library for creating high quality Encapsulated Postscript,
PDF, PNG, or SVG charts. It currently supports line plots, bar plots, 
range-fill plots, and pie charts. Because it is based on Python, you can make 
full use of Python's scripting power.

%package doc
Summary: Documentation for using pychart in python programs
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
PyChart is a Python library for creating high quality Encapsulated Postscript,
PDF, PNG, or SVG charts. It currently supports line plots, bar plots,
range-fill plots, and pie charts. Because it is based on Python, you can make
full use of Python's scripting power.

Install this package if you want the developers' documentation and examples
that tell you how to program with the pychart library.

%prep
%setup -q -n PyChart-1_39 -T -b 0 -a 1
%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build
cd demos/
make colorps colorpdf colorpng
cd ../doc
make

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{python_sitelib}/pychart/
%{python_sitelib}/PyChart-*.egg-info

%files doc
%defattr(-,root,root,-)
%doc doc/examples doc/pychart

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.39-10.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.39-8
- Rebuild for Python 2.6

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.39-7
- fix FTBFS bz 440754 (missing egg.info)

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.39-6
- license fix

* Fri Dec 22 2006 Jef Spaleta <jspaleta@gmail.com> 1.39-5
- bump for python 2.5 in development

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.39-4
- bump for FC-6

* Tue Jan 10 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.39-3
- FC3 doesn't need latex2html

* Mon Jan  9 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.39-2
- BR: tetex-latex, latex2html

* Mon Jan  9 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.39-1
- bump to 1.39

* Mon Sep 19 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 1.38-2
- Create a doc subpackage with the developers documentation

* Sat Sep 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.38-1
- initial package for Fedora Extras
