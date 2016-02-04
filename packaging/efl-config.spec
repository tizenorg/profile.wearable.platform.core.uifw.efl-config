Name:       efl-config
Summary:    EFL Config daemon
Version:    0.1
Release:    0
Group:      System/Libraries
License:    Apache-2.0
Source:     %{name}-%{version}.tar.gz
Source1: %{name}.service
Source2: %{name}.path
Source3: %{name}.manifest
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(elementary)
BuildRequires: pkgconfig(ecore-wayland)

%description
EFL config daemon

%prep
%setup -q
cp %{SOURCE3} .

%build
./autogen.sh
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_unitdir_user}/default.target.wants
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir_user}/%{name}.service
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir_user}/%{name}.path
ln -s ../%{name}.path %{buildroot}%{_unitdir_user}/default.target.wants/%{name}.path

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/bin/efl_config
%{_unitdir_user}/%{name}.service
%{_unitdir_user}/%{name}.path
%{_unitdir_user}/default.target.wants/%{name}.path
%manifest %{name}.manifest
