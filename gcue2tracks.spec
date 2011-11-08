Name:           gcue2tracks
Version:        0.5.0
Release:        1
License:        GPLv2+
Summary:        Tool for spliting audio CD image to tracks with cue sheet info
Url:            https://www.assembla.com/wiki/show/gCue2tracks
Group:          Sound
Source0:        http://trac-hg.assembla.com/gCue2tracks/raw-attachment/wiki/Archive/%{name}_%{version}.tar.gz
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
GUI for cue2tracks. Tool for spliting audio CD image to tracks with cue sheet info.

%prep
%setup -qn gCue2tracks

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
