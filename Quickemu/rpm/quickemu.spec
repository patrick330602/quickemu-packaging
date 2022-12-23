%define packager       Jinming Wu, Patrick <me@patrickwu.space>
%define maintainer     Martin Wimpress <code@wimpress.io>
Summary: Quickemu creates and runs optimised virtual machines.
Name: quickemu
Version: 4.5
Release: 0
Source: quickemu-4.5.tar.gz
BuildArch: noarch
Requires: qemu bash coreutils edk2-tools grep jq lsb procps python3 genisoimage usbutils util-linux sed spice-gtk-tools swtpm wget xdg-user-dirs xrandr unzip
BuildRoot: %{_tmppath}/%{name}-%{version}-build
URL: https://github.com/quickemu-project/quickemu
License: MIT

%description
Quickemu creates and runs optimised virtual machines.
Simple script to "manage" Qemu virtual machines. Each virtual machine
configuration is a few lines long requiring minimal setup. The main objective
of the project is to enable quick testing of desktop Linux distributions where
the virtual machines configuration and disk images can be stored anywhere,
such as external USB storage or your home directory. Windows and macOS guests
are also supported.

%prep
%setup -q

%build

%install
# for os <= 7
mkdir -p %{?buildroot}/usr/bin/
# normal part
install -Dm755 quickemu %{?buildroot}/usr/bin/quickemu
install -Dm755 quickget %{?buildroot}/usr/bin/quickget
install -Dm755 macrecovery %{?buildroot}/usr/bin/macrecovery

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/quickemu
%{_bindir}/quickget
%{_bindir}/macrecovery

%changelog
* Sun Dec 11 2022 Martin Wimpress <code@wimpress.io> - 4.5.1-0

  * New upstream release.
    + https://github.com/quickemu-project/quickemu/releases/tag/4.5


