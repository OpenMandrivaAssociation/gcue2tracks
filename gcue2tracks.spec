Name:           gcue2tracks
Version:        0.5.2
Release:        2
License:        GPLv2+
Summary:        Tool for spliting audio CD image to tracks with cue sheet info
Url:            https://www.assembla.com/wiki/show/gCue2tracks
Group:          Sound
Source0:        %{name}-%{version}.tar.xz
%py_requires
Requires:       cuetools
Requires:       ffmpeg
Requires:       pygtk2.0
Requires:       mutagen
Requires:       shntool
Suggests:       flac
Suggests:       vorbis-tools
Suggests:       wavpack
BuildArch:      noarch

%description
GUI for cue2tracks. Tool for spliting audio CD image to tracks with cue sheet
info.

%prep
%setup -q

%build

%install
# Don't use --record-rpm, this records standard dirs.
python setup.py install \
        --root=%{buildroot} \
        --prefix=%{_prefix} \
        --record=INSTALLED_FILES
rm -f %{buildroot}%{_datadir}/gcue2tracks/ui/*.h
%find_lang gCue2tracks

%files -f gCue2tracks.lang
%defattr(-,root,root,-)
%{_bindir}/gcue2tracks
%{_datadir}/applications/gCue2tracks.desktop
%{_datadir}/gcue2tracks
%{_datadir}/pixmaps/gCue2tracks.png
%{py_sitedir}/*
%doc debian/copyright changelog


%changelog
* Wed Jun 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.5.2-1
+ Revision: 803010
- update to 0.5.2

* Tue Nov 08 2011 Andrey Smirnov <asmirnov@mandriva.org> 0.5.0-1
+ Revision: 729061
- imported package gcue2tracks

