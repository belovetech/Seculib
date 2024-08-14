import type { DDOSAttempt } from '@/types'

export const ddosAttempts: DDOSAttempt[] = [
  {
    id: 1,
    ip_address: '192.168.1.1',
    request_count: 1500,
    attempt_date: '2024-08-14T10:00:00Z',
    attack_type: 'HTTP Flood',
    status: 'blocked'
  },
  {
    id: 2,
    ip_address: '192.168.1.2',
    request_count: 1200,
    attempt_date: '2024-08-14T10:05:00Z',
    attack_type: 'SYN Flood',
    status: 'blocked'
  },
  {
    id: 3,
    ip_address: '192.168.1.3',
    request_count: 2000,
    attempt_date: '2024-08-14T10:10:00Z',
    attack_type: 'UDP Flood',
    status: 'blocked'
  },
  {
    id: 4,
    ip_address: '192.168.1.4',
    request_count: 1800,
    attempt_date: '2024-08-14T10:15:00Z',
    attack_type: 'Ping of Death',
    status: 'blocked'
  },
  {
    id: 5,
    ip_address: '192.168.1.5',
    request_count: 2200,
    attempt_date: '2024-08-14T10:20:00Z',
    attack_type: 'HTTP Flood',
    status: 'blocked'
  },
  {
    id: 6,
    ip_address: '192.168.1.6',
    request_count: 1600,
    attempt_date: '2024-08-14T10:25:00Z',
    attack_type: 'SYN Flood',
    status: 'blocked'
  },
  {
    id: 7,
    ip_address: '192.168.1.7',
    request_count: 1400,
    attempt_date: '2024-08-14T10:30:00Z',
    attack_type: 'UDP Flood',
    status: 'blocked'
  },
  {
    id: 8,
    ip_address: '192.168.1.8',
    request_count: 2500,
    attempt_date: '2024-08-14T10:35:00Z',
    attack_type: 'Ping of Death',
    status: 'blocked'
  },
  {
    id: 9,
    ip_address: '192.168.1.9',
    request_count: 1300,
    attempt_date: '2024-08-14T10:40:00Z',
    attack_type: 'HTTP Flood',
    status: 'blocked'
  },
  {
    id: 10,
    ip_address: '192.168.1.10',
    request_count: 1700,
    attempt_date: '2024-08-14T10:45:00Z',
    attack_type: 'SYN Flood',
    status: 'blocked'
  }
]
