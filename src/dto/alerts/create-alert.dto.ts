import {
  IsString,
  IsBoolean,
  IsOptional,
  IsObject,
  IsDate,
} from 'class-validator';

export class CreateAlertDto {
  @IsString()
  prompt: string;

  @IsString()
  httpMethod: string;

  @IsString()
  httpUrl: string;

  @IsOptional()
  @IsObject()
  httpHeaders?: Record<string, any> | null;

  @IsOptional()
  @IsString()
  llmModel?: string;

  @IsBoolean()
  isRecurring: boolean;

  @IsOptional()
  @IsObject()
  payloadFormat?: Record<string, any> | null;

  @IsOptional()
  @IsDate()
  maxDatetime?: Date | null;
}
