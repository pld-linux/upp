Summary:	Ultimate++ - a C++ cross-platform rapid application development suite
#Summary(pl.UTF-8):	-
Name:		upp
Version:	2007.1
Release:	0.1
License:	BSD
Group:		Development
Source0:	http://dl.sourceforge.net/upp/%{name}-%{version}.tar.gz
# Source0-md5:	52e896525a3754bac265234e520278be
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-include_path.patch
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ultimate++ is a C++ cross-platform rapid application development suite
focused on programmers productivity. It includes a set of libraries
(GUI, SQL, etc..), and an integrated development environment. Rapid
development is achieved by the smart and aggressive use of C++ rather
than through fancy code generators. In this respect, U++ competes with
popular scripting languages while preserving C/C++ runtime
characteristics. The U++ integrated development environment, TheIDE,
introduces modular concepts to C++ programming. It features
BLITZ-build technology to speedup C++ rebuilds up to 4 times, Visual
designers for U++ libraries, Topic++ system for documenting code and
creating rich text resources for applications (like help and code
documentation) and Assist++ - a powerful C++ code analyzer that
provides features like code completion, navigation and transformation.
TheIDE can work with GCC, MinGW and Visual C++ 7.1 or 8.0 compilers
(including free Visual C++ Toolkit 2003 and Visual C++ 2005 Express
Edition) and contains a full featured debugger. TheIDE can also be
used to develop non-U++ applications. U++ distributions combine U++
with 3rd party tools like MinGW compiler or SDL library to provide an
instant development platform. What you can get with the Ultimate++
download in plain English Very effective C++ library for
cross-platform development in source form. A good integrated
development environment, designed for developing large C++
applications. You can use both, or you can use whichever you need.

#%%description -l pl.UTF-8

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	RPMCXXFLAGS="%{rpmcxxflags}" \
	libdir="%{_libdir}" \
	LIBPATH="-L%{_x_libraries}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/theide.desktop
%{_pixmapsdir}/theide.png
