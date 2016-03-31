Name:       efl-config
Summary:    EFL Config daemon
Version:    0.1
Release:    0
Group:      System/Libraries
License:    Apache-2.0
Source:     %{name}-%{version}.tar.gz
Source1: %{name}.path
Source2: %{name}.manifest
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(elementary)
BuildRequires: pkgconfig(ecore-wayland)
BuildRequires: pkgconfig(libtzplatform-config)

%description
EFL config daemon

%prep
%setup -q
cp %{SOURCE2} .

%build
./autogen.sh
TZ_SYS_BIN=%{TZ_SYS_BIN} ./configure --prefix %{_prefix}/

export TZ_SYS_RO_SHARE="%{TZ_SYS_RO_SHARE}"
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_unitdir_user}/default.target.wants
install -m 0644 %{_builddir}/%{name}-%{version}/packaging/%{name}.service %{buildroot}%{_unitdir_user}/%{name}.service
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir_user}/%{name}.path
ln -s ../%{name}.path %{buildroot}%{_unitdir_user}/default.target.wants/%{name}.path

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{TZ_SYS_BIN}/efl_config
%{_unitdir_user}/%{name}.service
%{_unitdir_user}/%{name}.path
%{_unitdir_user}/default.target.wants/%{name}.path
%manifest %{name}.manifest
