import {
  Entity,
  Column,
  PrimaryGeneratedColumn,
  CreateDateColumn,
} from 'typeorm';

@Entity('alerts')
export class AlertRequest {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ type: 'text' })
  prompt: string;

  @Column({ name: 'http_method' })
  httpMethod: string;

  @Column({ name: 'http_url' })
  httpUrl: string;

  @Column({ name: 'http_headers', type: 'jsonb', nullable: true })
  httpHeaders?: Record<string, any> | null;

  @Column({ name: 'llm_model', nullable: true })
  llmModel?: string;

  @Column({ name: 'is_recurring' })
  isRecurring: boolean;

  @Column({ name: 'payload_format', type: 'jsonb', nullable: true })
  payloadFormat?: Record<string, any> | null;

  @Column({ name: 'max_datetime', type: 'timestamp', nullable: true })
  maxDatetime?: Date | null;

  @CreateDateColumn({ name: 'created_at' })
  createdAt: Date;
}
