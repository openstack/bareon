# Copyright 2014 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import traceback


class BaseError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(BaseError, self).__init__(message, *args, **kwargs)


class InternalError(BaseError):
    def __init__(self, message=None, exc_info=True):
        if message is None:
            message = 'Internall error'
        if exc_info:
            self.exc_info = sys.exc_info()
            message += '\nOriginal exception {}'.format(
                ''.join(traceback.format_exception(*self.exc_info)))

        super(InternalError, self).__init__(message)


class DataSchemaCorruptError(InternalError):
    def __init__(self, message=None, **kwargs):
        if message is None:
            message = (
                'Integrity error in data processed by data validator. This '
                'mean an error in data validation scheme or in parsing code.')
        super(DataSchemaCorruptError, self).__init__(message, **kwargs)


class ApplicationDataCorruptError(BaseError):
    pass


class WrongInputDataError(BaseError):
    pass


class InputDataSchemaValidationError(WrongInputDataError):
    def __init__(self, defects):
        human_readable_defects = []
        for idx, d in enumerate(defects):
            path = list(d.path)
            path = '/'.join((str(x) for x in path))
            human_readable_defects.append(
                '{:>2} (/{}): {}'.format('#{}'.format(idx), path, d.message))

        indent = ' ' * 4
        separator = '\n{}'.format(indent)
        message = 'Invalid input data:\n{}{}'.format(
            indent, separator.join(human_readable_defects))

        super(WrongInputDataError, self).__init__(message, defects)
        self.defects = defects


class BlockDeviceNotFoundError(BaseError):
    def __init__(self, kind, needle):
        super(BlockDeviceNotFoundError, self).__init__(
            'Block device not found. Lookup details: '
            'kind="{}", needle="{}"'.format(kind, needle))
        self.kind = kind
        self.needle = needle


class BlockDeviceSchemeError(BaseError):
    pass


class BlockDeviceAllocationError(BlockDeviceSchemeError):
    pass


class WrongPartitionSchemeError(BaseError):
    pass


class WrongPartitionPolicyError(BaseError):
    pass


class PartitionSchemeMismatchError(BaseError):
    pass


class HardwarePartitionSchemeCannotBeReadError(BaseError):
    pass


class WrongPartitionLabelError(BaseError):
    pass


class PartitionNotFoundError(BaseError):
    pass


class DiskNotFoundError(BaseError):
    pass


class NotEnoughSpaceError(BaseError):
    pass


class PVAlreadyExistsError(BaseError):
    pass


class PVNotFoundError(BaseError):
    pass


class PVBelongsToVGError(BaseError):
    pass


class VGAlreadyExistsError(BaseError):
    pass


class VGNotFoundError(BaseError):
    pass


class LVAlreadyExistsError(BaseError):
    pass


class LVNotFoundError(BaseError):
    pass


class MDAlreadyExistsError(BaseError):
    pass


class MDNotFoundError(BaseError):
    pass


class MDDeviceDuplicationError(BaseError):
    pass


class MDWrongSpecError(BaseError):
    pass


class MDRemovingError(BaseError):
    pass


class WrongConfigDriveDataError(BaseError):
    pass


class WrongImageDataError(BaseError):
    pass


class TemplateWriteError(BaseError):
    pass


class ProcessExecutionError(BaseError):
    def __init__(self, stdout=None, stderr=None, exit_code=None, cmd=None,
                 description=None):
        self.exit_code = exit_code
        self.stderr = stderr
        self.stdout = stdout
        self.cmd = cmd
        self.description = description

        if description is None:
            description = ("Unexpected error while running command.")
        if exit_code is None:
            exit_code = '-'
        message = ('%(description)s\n'
                   'Command: %(cmd)s\n'
                   'Exit code: %(exit_code)s\n'
                   'Stdout: %(stdout)r\n'
                   'Stderr: %(stderr)r') % {'description': description,
                                            'cmd': cmd,
                                            'exit_code': exit_code,
                                            'stdout': stdout,
                                            'stderr': stderr}
        super(ProcessExecutionError, self).__init__(message)


class GrubUtilsError(BaseError):
    pass


class FsUtilsError(BaseError):
    pass


class HttpUrlConnectionError(BaseError):
    pass


class HttpUrlInvalidContentLength(BaseError):
    pass


class ImageChecksumMismatchError(BaseError):
    pass


class NoFreeLoopDevices(BaseError):
    pass


class WrongRepositoryError(BaseError):
    pass


class WrongDeviceError(BaseError):
    pass


class UnexpectedProcessError(BaseError):
    pass


class IncorrectChroot(BaseError):
    pass


class TooManyKernels(BaseError):
    pass


class EmptyCustomFlow(BaseError):
    pass


class NonexistingFlow(BaseError):
    pass


class WrongOutputContainer(BaseError):
    pass


class BootstrapFileAlreadyExists(BaseError):
    pass
