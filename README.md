Intel SDE Downloader
-------------

[![Build Status](https://travis-ci.org/marehr/intel-sde-downloader.svg?branch=master)](https://travis-ci.org/marehr/intel-sde-downloader)
![Python Versions](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6%2C%203.7%2C%203.8-blue.svg)

This tool will automatically download a version of [Intel SDE](https://software.intel.com/en-us/articles/intel-software-development-emulator/) from its [Download-Site](https://software.intel.com/protected-download/267266/144917).

A normal `wget` does not work, because the url of the download file is protected by a cookie-depending user-agreement.
This tool will auto-accept the "What If Pre-Release License Agreement" (cited below) and downloads the sde tarball.

Each version of Intel SDE has a certain LICENSE requirement and by using this script you should have read and accepted the license agreement beforehand. See the [download site](https://software.intel.com/en-us/articles/intel-software-development-emulator/) for the actual license.

Requirement and setup
---------

The downloader works with
* python 2.7 or ≥ python 3.4 and
* requires [MechanicalSoup](https://pypi.python.org/pypi/MechanicalSoup/) ≥ 0.9.0


Install the required libraries
```terminal
> pip install -r requirements.txt
```

Download a specific Intel SDE version
----------

```terminal
> python ./intel-sde-downloader.py sde-external-8.12.0-2017-10-23-lin.tar.bz2

Accept license
Attempt to download https://software.intel.com/system/files/managed/35/b2/sde-external-8.12.0-2017-10-23-lin.tar.bz2
Download written to sde-external-8.12.0-2017-10-23-lin.tar.bz2
```

List all available Intel SDE versions
----------

```terminal
> python ./intel-sde-downloader.py

Accept license

Not found: [EMPTY: NO ARGUMENT GIVEN]
Found versions:
sde-external-8.12.0-2017-10-23-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/35/b2/sde-external-8.12.0-2017-10-23-lin.tar.bz2">sde
-external-8.12.0-2017-10-23-lin.tar.bz2 (24.13 MB)</a>
sde-external-8.9.0-2017-08-06-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/6e/1f/sde-external-8.9.0-2017-08-06-lin.tar.bz2">sde-e
xternal-8.9.0-2017-08-06-lin.tar.bz2 (23.9 MB)</a>
sde-external-8.5.0-2017-06-08-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/45/15/sde-external-8.5.0-2017-06-08-lin.tar.bz2">sde-e
xternal-8.5.0-2017-06-08-lin.tar.bz2 (24.06 MB)</a>
sde-external-8.4.0-2017-05-23-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/2f/12/sde-external-8.4.0-2017-05-23-lin.tar.bz2">sde-e
xternal-8.4.0-2017-05-23-lin.tar.bz2 (24.01 MB)</a>
sde-external-7.58.0-2017-01-23-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/d7/1b/sde-external-7.58.0-2017-01-23-lin.tar.bz2">sde
-external-7.58.0-2017-01-23-lin.tar.bz2 (22.42 MB)</a>
sde-external-7.49.0-2016-07-07-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/2f/ac/sde-external-7.49.0-2016-07-07-lin.tar.bz2">sde
-external-7.49.0-2016-07-07-lin.tar.bz2 (22.09 MB)</a>
sde-external-7.45.0-2016-05-09-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/ec/75/sde-external-7.45.0-2016-05-09-lin.tar.bz2">sde
-external-7.45.0-2016-05-09-lin.tar.bz2 (22.15 MB)</a>
sde-external-7.41.0-2016-03-03-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/1e/ed/sde-external-7.41.0-2016-03-03-lin.tar.bz2">sde
-external-7.41.0-2016-03-03-lin.tar.bz2 (15.7 MB)</a>
sde-external-7.39.0-2016-01-18-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/c2/62/sde-external-7.39.0-2016-01-18-lin.tar.bz2">sde
-external-7.39.0-2016-01-18-lin.tar.bz2 (15.71 MB)</a>
2014-02-13-mpx-runtime-external-lin.tar.bz2 : <a href="https://software.intel.com/system/files/managed/91/b5/2014-02-13-mpx-runtime-external-lin.tar.bz2">2
014-02-13-mpx-runtime-external-lin.tar.bz2 (17.87 KB)</a>
```

License of download script
-----------

MIT


Copy of What If Pre-Release License Agreement of Intel SDE Version 8.12.0 [2017-10-23]
-------------

IMPORTANT - READ BEFORE COPYING, INSTALLING OR USING.

Do not copy, install, or use the "Materials" provided under this license agreement ("Agreement"), until you have carefully read the following terms and conditions. By copying, installing, or otherwise using the Materials, you agree to be bound by the terms of this Agreement. If you do not agree to the terms of this Agreement, do not copy, install, or use the Materials.

Pre-Release License Agreement for Pre-Release Software

1. PRE-RELEASE: The Materials are pre-release code, which may not be fully functional and which Intel may substantially modify in producing any final version. Intel can provide no assurance that it will ever produce or make generally available a final version.

2. LICENSE DEFINITIONS:

A. "Materials" are defined as the software, documentation, license key codes and other materials, including any updates and upgrade thereto, for the applicable pre-release software (which may be found at http://whatif.intel.com/), that are provided to you under this Agreement.

3. LICENSE GRANT:

A. Subject to all of the terms and conditions of this Agreement, Intel Corporation ("Intel") grants to you a non-exclusive, non-assignable copyright license to make only the minimum number of copies of the Materials reasonably necessary for your internal testing and development of your products.

B. Subject to all of the terms and conditions of this Agreement, Intel grants to you a non-exclusive, non-assignable copyright license to modify the Materials that are provided in source code (human readable) form.

C. If the Materials include the file named “redist.txt”, then subject to all of the terms and conditions of this Agreement and any specific restrictions which may appear in the “redist.txt” file, Intel grants to you a non-exclusive, non-assignable copyright license to redistribute the files (unmodified or modified by you) listed in the “redist.txt” file only as part of the application you develop with the Materials.

4. LICENSE RESTRICTIONS:

A. You may not reverse-assemble, reverse-compile, or otherwise reverse-engineer any software provided solely in binary form.

B. You may not distribute any portion of Materials, whether in source or binary form, to any third party, except as specified in this Agreement.

5. COPYRIGHT: Title to the Materials and all copies thereof remain with Intel or its suppliers. The Materials are copyrighted and are protected by United States copyright laws and international treaty provisions. You will not remove any copyright notice from the Materials. You agree to prevent any unauthorized copying of the Materials. Except as expressly provided herein, Intel does not grant any express or implied right to you under Intel patents, copyrights, trademarks, or trade secret information. Subject to Intel’s ownership of the Materials, all right, title and interest in and to your modifications shall belong to you.

6. REPLACEMENTS: The Materials are provided "AS IS" without warranty of any kind. If the media on which the Materials are furnished are found to be defective in material or workmanship under normal use for a period of ninety (90) days from the date of receipt, Intel's entire liability and your exclusive remedy shall be the replacement of the media. This offer is void if the media defect results from accident, abuse, or misapplication.

7. LIMITATION OF LIABILITY: THE ABOVE REPLACEMENT PROVISION IS THE ONLY WARRANTY OF ANY KIND. INTEL OFFERS NO OTHER WARRANTY EITHER EXPRESS OR IMPLIED INCLUDING THOSE OF MERCHANTABILITY, NONINFRINGEMENT OF THIRD- PARTY INTELLECTUAL PROPERTY OR FITNESS FOR A PARTICULAR PURPOSE. NEITHER INTEL NOR ITS SUPPLIERS SHALL BE LIABLE FOR ANY DAMAGES WHATSOEVER (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF BUSINESS PROFITS, BUSINESS INTERRUPTION, LOSS OF BUSINESS INFORMATION, OR OTHER LOSS) ARISING OUT OF THE USE OF OR INABILITY TO USE THE SOFTWARE, EVEN IF INTEL HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. BECAUSE SOME JURISDICTIONS PROHIBIT THE EXCLUSION OR LIMITATION OF LIABILITY FOR CONSEQUENTIAL OR INCIDENTAL DAMAGES, THE ABOVE LIMITATION MAY NOT APPLY TO YOU.

8. UNAUTHORIZED USE: THE MATERIALS ARE NOT DESIGNED, INTENDED, OR AUTHORIZED FOR USE IN ANY TYPE OF SYSTEM OR APPLICATION IN WHICH THE FAILURE OF THE MATERIALS COULD CREATE A SITUATION WHERE PERSONAL INJURY OR DEATH MAY OCCUR (E.G MEDICAL SYSTEMS, LIFE SUSTAINING OR LIFE SAVING SYSTEMS). Should the buyer purchase or use the Materials for any such unintended or unauthorized use, the buyer shall indemnify and hold Intel and its officers, subsidiaries and affiliates harmless against all claims, costs, damages, and expenses, and reasonable attorney fees arising out of, directly or indirectly, any claim of product liability, personal injury or death associated with such unintended or unauthorized use, even if such claim alleges that Intel was negligent regarding the design or manufacture of the part.

9. USER SUBMISSIONS: You agree that any material, information or other communication, including all data, images, sounds, text, and other things embodied therein, you transmit or post to an Intel website or provide to Intel under this Agreement will be considered non-confidential ("Communications"). Intel will have no confidentiality obligations with respect to the Communications. You agree that Intel and its designees will be free to copy, modify, create derivative works, publicly display, disclose, distribute, license and sublicense through multiple tiers of distribution and licensees, incorporate and otherwise use the Communications, including derivative works thereto, for any and all commercial or non-commercial purposes.

10. TERMINATION OF THIS LICENSE: The term of this Agreement will commence on the date this Agreement is accepted by You and will continue until terminated. This Agreement will terminate without notice on the last day of the pre-release period, which is specified elsewhere in the Materials, or upon the commercial release of the Materials. Intel may terminate this Agreement at any time, with or without cause, with written notice to you. Upon termination, you will immediately destroy the Materials or return all copies of the Materials to Intel along with any copies you have made.

11. U.S. GOVERNMENT RESTRICTED RIGHTS: The Materials are provided with "RESTRICTED RIGHTS". Use, duplication or disclosure by the Government is subject to restrictions set forth in FAR52.227-14 and DFAR252.227-7013 et seq. or its successor. Use of the Materials by the Government constitutes acknowledgment of Intel's rights in them.

12. EXPORT RESTRICTED RIGHTS: This software is subject to the U.S. Export Administration Regulations and other U.S. law, and may not be exported or re-exported to certain countries (Burma, Cuba, Iran, North Korea, Sudan, and Syria) or to persons or entities prohibited from receiving U.S. exports (including Denied Parties, Specially Designated Nationals, and entities on the Bureau of Export Administration Entity List or involved with missile technology or nuclear, chemical or biological weapons).

13. APPLICABLE LAWS: Any claim arising under or relating to this Agreement shall be governed by the internal substantive laws of the State of Delaware or federal courts located in Delaware, without regard to principles of conflict of laws. You may not export the Materials in violation of applicable export laws.

* Other names and brands may be claimed as the property of others
