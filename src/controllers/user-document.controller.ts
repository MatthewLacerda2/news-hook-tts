import { Body, Controller, Post } from '@nestjs/common';
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';

@ApiTags('user-documents')
@Controller('user-documents')
export class UserDocumentController {
  @Post()
  @ApiOperation({ summary: 'Create a new document' })
  @ApiResponse({
    status: 201,
    description: 'Document received successfully',
  })
  create(
    @Body('name') name: string,
    @Body('content') content: string,
  ): { success: boolean } {
    console.log('Received document:', { name, content });
    return { success: true };
  }
}
