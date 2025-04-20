import { PhoneNumber } from './phoneType'

export type DataSetupType = {
  companyName: string
  companyMainPhone: PhoneNumber
  companySecondPhone?: PhoneNumber
  companyLogo?: string
}
