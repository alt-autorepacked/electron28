# TODO: build from sources
Name: electron28
Version: 28.2.10
Release: alt2

Summary: Build cross platform desktop apps with JavaScript, HTML, and CSS

License: MIT
Url: https://electronjs.org/
Group: Development/Other

# Source-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-x64.zip
Source: %name-%version.tar

%define supported_arch x86_64

%set_verify_elf_method skip
%global __find_debuginfo_files %nil

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

BuildRequires: patchelf
BuildRequires: libgtk+3 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf
BuildRequires: libdrm libgbm
# bundled:
# library libnode.so not found
# library libffmpeg.so not found

%description
Build cross platform desktop apps with JavaScript, HTML, and CSS.

%prep
%setup -c

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/electron %buildroot/%_bindir/%name

patchelf --set-rpath '%_libdir/%name' %buildroot%_bindir/%name
#chmod -v 4711

%files
%ifarch %supported_arch
%_bindir/%name
%attr(4711,root,root) %_libdir/%name/chrome-sandbox
%attr(0755,root,root) %_libdir/%name/chrome_crashpad_handler
%attr(0755,root,root) %_libdir/%name/electron
%_libdir/%name/
%endif

%changelog
* Wed May 08 2024 Maxim Slipenko <noreply@maxim.slipenko.com> 28.2.10-alt2
- fix rights (alt-autorepacked/electron28#1)

* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 28.2.10-alt1
- new version 28.2.10 (with rpmrb script)

* Tue Mar 26 2024 Vitaly Lipatov <lav@altlinux.ru> 28.2.8-alt1
- new version 28.2.8 (with rpmrb script)

* Mon Dec 11 2023 Vitaly Lipatov <lav@altlinux.ru> 28.0.0-alt1
- initial build 28.x for ALT Sisyphus
