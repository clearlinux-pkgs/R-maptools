#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-maptools
Version  : 0.9.2
Release  : 27
URL      : https://cran.r-project.org/src/contrib/maptools_0.9-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/maptools_0.9-2.tar.gz
Summary  : Tools for Reading and Handling Spatial Objects
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-maptools-lib
Requires: R-sp
BuildRequires : R-sp
BuildRequires : clr-R-helpers

%description
This file is intended to clarify ownership and copyright: where
possible individual files also carry brief copyright notices.

%package lib
Summary: lib components for the R-maptools package.
Group: Libraries

%description lib
lib components for the R-maptools package.


%prep
%setup -q -c -n maptools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523315543

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523315543
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maptools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maptools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maptools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library maptools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || : || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/maptools/ChangeLog
/usr/lib64/R/library/maptools/DESCRIPTION
/usr/lib64/R/library/maptools/INDEX
/usr/lib64/R/library/maptools/Meta/Rd.rds
/usr/lib64/R/library/maptools/Meta/data.rds
/usr/lib64/R/library/maptools/Meta/features.rds
/usr/lib64/R/library/maptools/Meta/hsearch.rds
/usr/lib64/R/library/maptools/Meta/links.rds
/usr/lib64/R/library/maptools/Meta/nsInfo.rds
/usr/lib64/R/library/maptools/Meta/package.rds
/usr/lib64/R/library/maptools/Meta/vignette.rds
/usr/lib64/R/library/maptools/NAMESPACE
/usr/lib64/R/library/maptools/R/maptools
/usr/lib64/R/library/maptools/R/maptools.rdb
/usr/lib64/R/library/maptools/R/maptools.rdx
/usr/lib64/R/library/maptools/README
/usr/lib64/R/library/maptools/changes
/usr/lib64/R/library/maptools/data/SplashDams.rda
/usr/lib64/R/library/maptools/data/gpcholes.rda
/usr/lib64/R/library/maptools/data/state.vbm.rda
/usr/lib64/R/library/maptools/data/wrld_simpl.rda
/usr/lib64/R/library/maptools/doc/combine_maptools.R
/usr/lib64/R/library/maptools/doc/combine_maptools.Rnw
/usr/lib64/R/library/maptools/doc/combine_maptools.pdf
/usr/lib64/R/library/maptools/doc/index.html
/usr/lib64/R/library/maptools/grids/simple.ag
/usr/lib64/R/library/maptools/grids/test.ag
/usr/lib64/R/library/maptools/help/AnIndex
/usr/lib64/R/library/maptools/help/aliases.rds
/usr/lib64/R/library/maptools/help/maptools.rdb
/usr/lib64/R/library/maptools/help/maptools.rdx
/usr/lib64/R/library/maptools/help/paths.rds
/usr/lib64/R/library/maptools/html/00Index.html
/usr/lib64/R/library/maptools/html/R.css
/usr/lib64/R/library/maptools/libs/symbols.rds
/usr/lib64/R/library/maptools/shapes/Testing.kml
/usr/lib64/R/library/maptools/shapes/baltim.dbf
/usr/lib64/R/library/maptools/shapes/baltim.shp
/usr/lib64/R/library/maptools/shapes/baltim.shx
/usr/lib64/R/library/maptools/shapes/co37_d90.dbf
/usr/lib64/R/library/maptools/shapes/co37_d90.shp
/usr/lib64/R/library/maptools/shapes/co37_d90.shx
/usr/lib64/R/library/maptools/shapes/co45_d90.dbf
/usr/lib64/R/library/maptools/shapes/co45_d90.shp
/usr/lib64/R/library/maptools/shapes/co45_d90.shx
/usr/lib64/R/library/maptools/shapes/co51_d90.dbf
/usr/lib64/R/library/maptools/shapes/co51_d90.shp
/usr/lib64/R/library/maptools/shapes/co51_d90.shx
/usr/lib64/R/library/maptools/shapes/columbus.dbf
/usr/lib64/R/library/maptools/shapes/columbus.shp
/usr/lib64/R/library/maptools/shapes/columbus.shx
/usr/lib64/R/library/maptools/shapes/fylk-val-ll.dbf
/usr/lib64/R/library/maptools/shapes/fylk-val-ll.shp
/usr/lib64/R/library/maptools/shapes/fylk-val-ll.shx
/usr/lib64/R/library/maptools/shapes/fylk-val.dbf
/usr/lib64/R/library/maptools/shapes/fylk-val.shp
/usr/lib64/R/library/maptools/shapes/fylk-val.shx
/usr/lib64/R/library/maptools/shapes/pointZ.dbf
/usr/lib64/R/library/maptools/shapes/pointZ.prj
/usr/lib64/R/library/maptools/shapes/pointZ.shp
/usr/lib64/R/library/maptools/shapes/pointZ.shx
/usr/lib64/R/library/maptools/shapes/sids.dbf
/usr/lib64/R/library/maptools/shapes/sids.shp
/usr/lib64/R/library/maptools/shapes/sids.shx
/usr/lib64/R/library/maptools/share/90mfips.txt
/usr/lib64/R/library/maptools/share/Splus.map
/usr/lib64/R/library/maptools/share/co37_d90.e00
/usr/lib64/R/library/maptools/share/gshhs_c.b
/usr/lib64/R/library/maptools/share/nc_xtra.dbf
/usr/lib64/R/library/maptools/share/wdb_borders_c.b

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/maptools/libs/maptools.so
/usr/lib64/R/library/maptools/libs/maptools.so.avx2
/usr/lib64/R/library/maptools/libs/maptools.so.avx512
