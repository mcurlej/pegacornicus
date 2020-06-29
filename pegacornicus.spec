Name:           pegacornicus
Version:        0.0.3
Release:        1%{?dist}
Summary:        Hello World for RPM

License:        MIT
URL:            https://github.com/mcurlej/%{name}
%_disable_source_fetch 0
%_urlhelper %{__urlhelpercmd} %{?__urlhelper_localopts} -L %{?__urlhelper_proxyopts} %{__urlhelperopts}
Source0:        https://github.com/mcurlej/%{name}/archive/dev.tar.gz

BuildRequires:  python
Requires:       python
Requires:       bash

BuildArch:      noarch

%description
Hello World for RPM


%prep
%autosetup -n pegacornicus-dev


%build

python -m compileall app.py

%install

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}/%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/app.pyc
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

install -m 0644 app.py* %{buildroot}/usr/lib/%{name}/

%files
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/app.py*


%changelog
* Mon Mar  9 2020 Martin Curlej <mcurlej@redhat.com>
- First Pegacornicus package
