import { Body, Controller, Post } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { AlertEvent } from '../entities/alert-event.entity';
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';

@ApiTags('alert-events')
@Controller('alert-events')
export class AlertEventsController {
  constructor(
    @InjectRepository(AlertEvent)
    private alertEventRepository: Repository<AlertEvent>,
  ) {}

  @Post()
  @ApiOperation({ summary: 'Webhook endpoint for alert events' })
  @ApiResponse({
    status: 201,
    description: 'Payload received and stored',
    type: AlertEvent,
  })
  async create(@Body() payload: any): Promise<AlertEvent> {
    const alertEvent = new AlertEvent();
    alertEvent.payload = payload as Record<string, any>;

    return this.alertEventRepository.save(alertEvent);
  }
}
