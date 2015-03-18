Summary:	GNU patch Utilities
Name:		patch
Version:	2.7.5
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz
# Source0-md5:	e3da7940431633fb65a01b91d3b7a27a
URL:		http://www.gnu.org/software/patch/patch.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Patch is a program to aid in patching programs. You can use it to
apply 'diff's. Basically, you can use diff to note the changes in a
file, send the changes to someone who has the original file, and they
can use 'patch' to combine your changes to their original.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	man1dir=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

