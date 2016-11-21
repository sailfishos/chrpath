Name:       chrpath
Summary:    Modify rpath of compiled programs
Version:    0.16
Release:    3
Group:      Development/Tools
License:    GPL+
URL:        https://chrpath.alioth.debian.org/
Source0:    https://alioth.debian.org/frs/download.php/file/3979/%{name}-%{version}.tar.gz

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q -n %{name}-%{version}

%build

autoreconf -v -f -i
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -fr %{buildroot}/usr/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README 
%{_bindir}/chrpath
%doc %{_mandir}/man1/chrpath.1*

