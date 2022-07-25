%define repo github.com/ipfs/kubo
# golang specifics
%global golang_version 1.18
#debuginfo not supported with Go
%global debug_package %{nil}


Name:           kubo
Version:        0.14.0
Release:        1%{?dist}
Summary:        IPFS implementation in Go

License:        MIT
URL:            https://%{repo}
Source0:        https://%{repo}/archive/v%{version}.tar.gz

BuildRequires: git
BuildRequires: systemd
BuildRequires: golang >= %{golang_version}

%description
IPFS implementation in Go

%prep
%setup -q -c
mkdir -p $(dirname src/%{repo})
mv %{name}-%{version} src/%{repo}

%build
export GOPATH="$(pwd)"
export PATH=$PATH:"$(pwd)"/bin
cd src/%{repo}
make build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

cp src/github.com/ipfs/kubo/cmd/ipfs/ipfs %{buildroot}%{_bindir}
cat << EOF >> %{buildroot}%{_unitdir}/ipfs.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/bin/ipfs daemon
Restart=on-failure
Type=notify
NotifyAccess=all

[Install]
WantedBy=default.target
EOF

%post

%systemd_post ipfs.service

%preun

%systemd_preun ipfs.service

%files
%{_bindir}/ipfs
%{_unitdir}/ipfs.service
%license src/%{repo}/LICENSE-MIT

%changelog
* Mon Jul 25 2022 Oleg Silkin <osilkin@redhat.com> - 0.14.0-1
- 🛠️ BREAKING CHANGES
  - Removed mdns_legacy implementation
- 🔦 Highlights
  - 🛣️ Delegated Routing
  - 👥 Rename to Kubo
  - 🎒 ipfs repo migrate
  - 🚀 Emoji support in Multibase


* Thu Apr 28 2022 Ryan Cook <rcook@redhat.com> 0.12.2-2
- Version bump

* Mon Apr 4 2022 Ryan Cook <rcook@redhat.com> 0.12.1-1
- Fork of https://github.com/daftaupe/go-ipfs-rpm and version bump

* Fri Jul 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.16-1
- Update to version 0.4.16

* Sun May 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.15-2
- Change changelog
- Fix description

* Sat May 12 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.15-1
- Update to version 0.4.15

* Tue Apr 10 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.14-1
- Initial rpm : version 0.4.14
