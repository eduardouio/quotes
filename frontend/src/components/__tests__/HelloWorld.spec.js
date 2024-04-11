import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ProfileView from '@/views/ProfileView.vue'

describe('ProfileView', () => {
  it('renders properly', () => {
    const wrapper = mount(ProfileView, {})
    expect(wrapper.html()).toContain('div')
  })
})
