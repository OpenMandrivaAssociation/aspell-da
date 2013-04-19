%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver %{version}
%define fname new_aspell-da
%define aspell_ver 0.60
%define languagelocal dansk
%define languageeng danish
%define languageenglazy Danish
%define languagecode da

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.7.42
Release:       2
Epoch:	       1
Group:         System/Internationalization
Source:        http://da.speling.org/filer/new_aspell-da-%version.tar.bz2
URL:           http://da.speling.org/
License:       GPL
Provides: spell-da

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary aspell-dk

# RedHat Stuff.
#Obsoletes: ispell-dk, ispell-danish
Obsoletes: aspell-dk

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.6.19-5mdv2011.0
+ Revision: 662804
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.6.19-4mdv2011.0
+ Revision: 603199
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.6.19-3mdv2010.1
+ Revision: 518913
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.6.19-2mdv2010.0
+ Revision: 413059
- rebuild

* Fri Nov 14 2008 Funda Wang <fwang@mandriva.org> 1:1.6.19-1mdv2009.1
+ Revision: 303227
- new version 1.6.19

* Sun Aug 10 2008 Funda Wang <fwang@mandriva.org> 1:1.6.16-1mdv2009.0
+ Revision: 270148
- New version 1.6.16

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:1.4.42.1-6mdv2009.0
+ Revision: 220368
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1:1.4.42.1-5mdv2008.1
+ Revision: 182411
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:1.4.42.1-4mdv2008.1
+ Revision: 148745
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.42.1-3mdv2007.0
+ Revision: 124099
- rebuilt due to bs fjukiness
- Import aspell-da

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.42.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.4.42.1-1mdk
- new release

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-7mdk
- updated

