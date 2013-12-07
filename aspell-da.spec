%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver %{version}
%define fname new_aspell-da
%define aspell_ver 0.60
%define languagelocal dansk
%define languageeng danish
%define languageenglazy Danish
%define languagecode da

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	1.7.42
Release:	6
Epoch:		1
Group:		System/Internationalization
License:	GPLv2
Url:		http://da.speling.org/
Source0:	http://da.speling.org/filer/new_aspell-da-%version.tar.bz2
BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-dk
Provides:	spell-da
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure
%make

%install
%makeinstall_std
chmod 644 README Copyright

%files
%doc README*
%{_libdir}/aspell-%{aspell_ver}/*

